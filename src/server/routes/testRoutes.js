// import { test } from "../controllers/testController.js";
import { uploadFile } from "../controllers/fileController.js";
import express from 'express';
import multer from 'multer';

const router = express.Router();

router.route('/').post(multer().any(), uploadFile);

export default router;