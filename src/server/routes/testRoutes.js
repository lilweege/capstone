import { test } from "../controllers/testController.js";
import express from 'express';
import multer from 'multer';

const router = express.Router();

router.route('/').get(multer().any(), test);

export default router;