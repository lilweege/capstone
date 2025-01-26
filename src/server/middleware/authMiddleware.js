export const checkJwt = auth({
    audience: process.env.AUTH0_AUDIENCE,
    issuerBaseURL: `https://${process.env.AUTH0_DOMAIN}/`,
});

// Error handler for invalid or expired JWT
export const jwtErrorHandler = (err, req, res, next) => {
    if (err.name === 'UnauthorizedError') {
        // JWT token is missing, expired, or invalid
        return res.status(401).json({
            error: 'Unauthorized',
            message: 'Invalid or missing token. Please provide a valid JWT token.'
        });
    }
    next(err); // If the error is not related to JWT, pass it to the next handler
};