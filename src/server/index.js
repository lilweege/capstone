import express from "express";
import cors from "cors";
import { auth } from "express-oauth2-jwt-bearer";
import { loggerMiddleware } from "./middleware/loggerMiddleware.js";
import { apiUrlFor } from "./utilities/apiUtils.js";
import { AuthVariables, SystemVariables } from "./constants/envConstants.js";
import uploadApi from "./controllers/uploadController.js";

import { UnauthorizedException } from "./types/exceptions.js";
import { ErrorContent } from "./types/errorContent.js";

const app = express();
app.use(cors());

// JWT Authentication Middleware
const checkJwt = auth({
  audience: AuthVariables.AUTH0_AUDIENCE,
  issuerBaseURL: `https://${AuthVariables.AUTH0_DOMAIN}/`,
});

// Error handler for invalid or expired JWT
const jwtErrorHandler = (err, req, res, next) => {
  if (err.name === "UnauthorizedError") {
    const customError = new UnauthorizedException(
      "Invalid or missing token. Please provide a valid JWT token.",
      "INVALID_JWT_TOKEN"
    );

    const errorContent = ErrorContent.convertFromException(customError);
    return res.status(errorContent.status).json(errorContent.getSummary());
  }
  next(err);
};

// Use the checkJwt middleware to protect routes
app.use(checkJwt);
app.use(jwtErrorHandler);

app.use(loggerMiddleware);
app.use(express.json());
app.use(apiUrlFor("upload"), uploadApi);

app.use((err, req, res, next) => {
  const errorContent = ErrorContent.convertFromException(err);
  res.status(errorContent.status).json(errorContent.getSummary());
});

app.listen(SystemVariables.PORT, () => {
  console.log("Server listening on port", SystemVariables.PORT);
});

export default app;
