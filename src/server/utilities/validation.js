import fs from 'fs';

export const validatePythonFiles = (filePath, maxLines) => {
    const content = fs.readFileSync(filePath, 'utf8');
    const lines = content.split('\n');
    if (lines.length > maxLines) {
        throw new Error(`File ${filePath} exceeds ${maxLines} lines.`);
    }
};

export const validateFileCount = (files, maxFiles) => {
    if (files.length > maxFiles) {
        throw new Error(`Too many files in the archive (max: ${maxFiles}).`);
    }
};
