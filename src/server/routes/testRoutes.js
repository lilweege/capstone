import { test } from "../controllers/testController.js";
import express from 'express';

const testRouter = express.Router();

testRouter.get('/', test);

export default testRouter;