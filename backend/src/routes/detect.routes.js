import { Router } from "express";
import { upload } from "../middleware/multer.middleware.js";

const detectRoute = Router();

// Import controllers
import { Detection } from "../models/detection.models.js";

// Secure routes
detectRoute.route("/detection").post(upload.single("ImageToDetect"), Detection);

export default detectRoute;
