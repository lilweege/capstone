import express from 'express';
import cors from 'cors';
// import { auth } from 'express-oauth2-jwt-bearer';
import testRouter from './routes/testRoutes.js';
import { loggerMiddleware } from './middleware/loggerMiddleware.js';

const app = express();
app.use(cors());

/*
// JWT Authentication Middleware
const checkJwt = auth({
    audience: process.env.AUTH0_AUDIENCE,
    issuerBaseURL: `https://${process.env.AUTH0_DOMAIN}/`,
});

// Error handler for invalid or expired JWT
const jwtErrorHandler = (err, req, res, next) => {
    if (err.name === 'UnauthorizedError') {
        // JWT token is missing, expired, or invalid
        return res.status(401).json({
            error: 'Unauthorized',
            message: 'Invalid or missing token. Please provide a valid JWT token.'
        });
    }
    next(err); // If the error is not related to JWT, pass it to the next handler
};

// Use the checkJwt middleware to protect routes
app.use(checkJwt);

// Middleware for handling invalid JWT token errors
app.use(jwtErrorHandler);
*/
app.use(loggerMiddleware);
app.use(express.json());
app.use('/test', testRouter);

app.listen(8080, () => {
    console.log('Server listening on port 8080');
});

export default app;