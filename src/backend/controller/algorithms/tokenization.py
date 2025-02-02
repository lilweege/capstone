#!/usr/bin/env python3
from enum import Enum
import sys
import argparse
import tokenize
from itertools import combinations
from dataclasses import dataclass

@dataclass
class Fingerprint:
    hash_val: int
    position: int


class NormalizedTokenType(Enum):
    IDENTIFIER = 0
    NUMERIC_LITERAL = 1
    STRING_LITERAL = 2

@dataclass
class Token:
    start_pos: tuple[int, int]
    end_pos: tuple[int, int]
    value: str | NormalizedTokenType


class Tokenizer:
    def _normalize_token(self, tok_type, tok_string):
        # Token types from the built-in tokenize module
        if tok_type == tokenize.NAME:
            # Use the keyword module to check if the token is a keyword.
            import keyword
            if keyword.iskeyword(tok_string):
                return tok_string
            else:
                return NormalizedTokenType.IDENTIFIER
        elif tok_type == tokenize.NUMBER:
            return NormalizedTokenType.NUMERIC_LITERAL
        elif tok_type == tokenize.STRING:
            return NormalizedTokenType.STRING_LITERAL
        elif tok_type in (tokenize.NEWLINE, tokenize.NL, tokenize.ENCODING):
            return ""
        else:
            return tok_string.strip()


    def _hash_token(self, token: Token) -> int:
        if isinstance(token.value, NormalizedTokenType):
            return token.value.value
        assert isinstance(token.value, str)
        BASE = 747287
        MOD = 33554393
        hsh = 0
        for ch in token.value:
            hsh = ((hsh + ord(ch)) * BASE) % MOD
        return hsh


    def _tokenize_file(self, file_path: str) -> tuple[list[Token], set[str]]:
        """
        Tokenizes the given Python file and returns a list of token strings.
        """
        comments = set()
        tokens = []
        try:
            with open(file_path, 'rb') as f:
                token_generator = tokenize.tokenize(f.readline)
                for tok in token_generator:
                    # Ignore tokens we don’t care about.
                    if tok.type == tokenize.COMMENT:
                        # Handle comments specially, we want to check for lazy exact matches
                        comments.add(tok.string)
                    if tok.type in (tokenize.COMMENT, tokenize.NL, tokenize.NEWLINE, tokenize.ENCODING):
                        continue
                    normalized = self._normalize_token(tok.type, tok.string)

                    if normalized != "":
                        tokens.append(Token(tok.start, tok.end, normalized))
        except Exception as e:
            print(f"Error tokenizing {file_path}: {e}", file=sys.stderr)

        return tokens, comments


    def _compute_rolling_hashes(self, tokens: list[Token], k: int) -> list[Fingerprint]:
        """
        Computes a list of rolling hash values for all k-grams in the token list. The hash for a k-gram is computed using Rabin-Karp.
        Returns a list of Fingerprint(hash_val, position) for each k-gram starting at index position.
        """
        n = len(tokens)
        if n < k:
            return []

        BASE = 4194301
        MOD = 33554393

        hashes = []
        high_order = pow(BASE, k - 1, MOD)
        
        h = 0
        for i in range(k):
            token_val = self._hash_token(tokens[i])
            h = (h * BASE + token_val) % MOD
        hashes.append(Fingerprint(hash_val=h, position=0))
        
        for i in range(1, n - k + 1):
            left_token_val = self._hash_token(tokens[i - 1])
            h = (h - left_token_val * high_order) % MOD
            h = (h * BASE + self._hash_token(tokens[i + k - 1])) % MOD
            hashes.append(Fingerprint(hash_val=h, position=i))

        return hashes


    def _winnowing(self, tokens: list[Token], k: int, w: int) -> dict[int, int]:
        """
        Implements the winnowing algorithm with a Rabin-Karp rolling hash.
        
        1. Computes rolling hash values over all k-grams.
        2. Slides a window of size w over the list of k-gram hashes and records the minimal hash in that window.
        
        Returns a dictionary mapping the starting position (index of the k-gram) to the fingerprint hash.
        """
        kgram_hashes = self._compute_rolling_hashes(tokens, k)
        n = len(kgram_hashes)
        fingerprints: dict[int, int] = {}
        
        if n == 0:
            return fingerprints
        
        if n < w:
            # If there are fewer than w hashes, choose the minimal one.
            min_fp = min(kgram_hashes, key=lambda fp: fp.hash_val)
            fingerprints[min_fp.position] = min_fp.hash_val
        else:
            # Slide a window over the k-gram hashes.
            for i in range(n - w + 1):
                window = kgram_hashes[i:i+w]
                min_fp = min(window, key=lambda fp: fp.hash_val)
                fingerprints[min_fp.position] = min_fp.hash_val

        return fingerprints


    def index_files(self, file_paths: list[str], k: int, w: int) -> tuple[dict[str, set[int]], dict[str, set[str]]]:
        """
        Processes each file: tokenizes, fingerprints, and then builds an index of fingerprints.
        
        Returns:
        - file_fingerprints: dict mapping file_path to its set of fingerprint hash values.
        - file_comments
        """
        file_fingerprints = {}
        file_comments = {}

        for file_path in file_paths:
            tokens, comments = self._tokenize_file(file_path)
            fingerprints = self._winnowing(tokens, k, w)
            file_fingerprints[file_path] = set(fingerprints.values())
            file_comments[file_path] = comments
        return file_fingerprints, file_comments


    def report_similarity(self, file_fingerprints: dict[str, set[int]], file_comments: dict[str, set[int]], min_common_percent: float) -> list[tuple[str, str, float]]:
        """
        Compares the fingerprint sets from each file pair and reports those with at least
        min_common shared fingerprints.
        """
        report = []
        files = list(file_fingerprints.keys())
        for file1, file2 in combinations(files, 2):
            common_fingerprints = file_fingerprints[file1] & file_fingerprints[file2]
            common_comments = file_comments[file1] & file_comments[file2]
            min_fingerprints = min(len(file_fingerprints[file1]), len(file_fingerprints[file2]))
            denominator = min_fingerprints + len(common_comments)
            if denominator > 0:
                similarity_score = (len(common_fingerprints) + len(common_comments)) / denominator
                if similarity_score >= min_common_percent:
                    report.append((file1, file2, similarity_score))
        return report



def main():
    parser = argparse.ArgumentParser(description="Prototype for tokenization-based similarity scoring.")
    parser.add_argument('files', metavar='FILE', nargs='+', help='Python source files to process')
    parser.add_argument('--k', type=int, default=23, help='k-gram size for fingerprinting (default: 23)') # 5
    parser.add_argument('--w', type=int, default=17, help='Window size for winnowing (default: 17)') # 4
    parser.add_argument('--m', type=float, default=0.5, help='Minimum percentage of common fingerprints to report similarity (default: 0.5)')
    
    args = parser.parse_args()

    tokenizer = Tokenizer()
    file_fingerprints, file_comments = tokenizer.index_files(args.files, k=args.k, w=args.w)
    
    similarities = tokenizer.report_similarity(file_fingerprints, file_comments, min_common_percent=args.m)
    for file1, file2, score in sorted(similarities, key=lambda x: -x[2]):
        print(f"{file1} {file2}:\n{score}")

if __name__ == '__main__':
    main()
