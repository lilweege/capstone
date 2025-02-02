import dotenv from "dotenv";

dotenv.config();

export class EmailVariables {
  static EMAIL_USER = process.env.EMAIL_USER;
  static EMAIL_PASS = process.env.EMAIL_PASS;
}

export class AuthVariables {
  static AUTH0_AUDIENCE = process.env.AUTH0_AUDIENCE;
  static AUTH0_DOMAIN = process.env.AUTH0_DOMAIN;
}

export class SystemVariables {
  static PORT = process.env.PORT;
}
