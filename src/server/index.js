import express from 'express';
import cors from 'cors';
// import { auth } from 'express-oauth2-jwt-bearer';
import router from './routes/testRoutes.js';
import { loggerMiddleware } from './middleware/index.js';

const app = express();
app.use(cors());

// // Use the checkJwt middleware to protect routes
// app.use(checkJwt);

// // Middleware for handling invalid JWT token errors
// app.use(jwtErrorHandler);
app.use(loggerMiddleware);
app.use(express.json());
app.use('/upload', router);

app.listen(8080, () => {
    console.log('Server listening on port 8080');
});

export default app;