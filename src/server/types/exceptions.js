export class HttpRequestException {
  constructor(status, message, code, details) {
    this.status = status;
    this.message = message;
    this.code = code;
    this.details = details;
  }
}

export class NotFoundException extends HttpRequestException {
  constructor(message, code, details) {
    super(404, message, code, details);
  }
}

export class BadRequestException extends HttpRequestException {
  constructor(message, code, details) {
    super(400, message, code, details);
  }
}

export class UnauthorizedException extends HttpRequestException {
  constructor(message, code, details) {
    super(401, message, code, details);
  }
}

export class ForbiddenException extends HttpRequestException {
  constructor(message, code, details) {
    super(403, message, code, details);
  }
}

export class Exception {
  constructor(message, code) {
    this.message = message;
    this.code = code;
  }
}