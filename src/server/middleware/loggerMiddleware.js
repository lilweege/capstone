import responseTime from 'response-time';
import logger from '../utilities/loggerUtils.js';

export const loggerMiddleware = (req, res, next) => {
  const { method, url } = req;

  // Log the request start
  logger.info(`Started ${method} ${url}`);

  // Use response-time to log the request completion
  responseTime((req, res, time) => {
    const { statusCode } = res;
    const logMessage = `Completed ${method} ${url} ${statusCode} in ${time.toFixed(2)}ms`;
    logger.info(logMessage);
  })(req, res, next);
};