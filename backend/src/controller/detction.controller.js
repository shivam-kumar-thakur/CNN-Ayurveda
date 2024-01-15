import { asyncHandler } from "../utils/asyncHandler.js";
import {ApiError} from "../utils/ApiError.js"
import {uploadOnCloudinary} from "../utils/cloudinary.js"
import { ApiResponse } from "../utils/ApiResponse.js";
import { Detection } from "../models/detection.models.js";
import { LeavesData } from "../models/dataLeaves.models.js";
import mongoose from "mongoose";



const detection=asyncHandler(async (req,res)=>{
    //upload the file to cloudinary
    console.log(req.files?.ImageToDetect);
    const imageLoacalPath=req.files?.ImageToDetect[0]?.path
    if(!imageLoacalPath)
    {
        throw new ApiError(400,"Image is required")
    }
    const imageUploadedUrl=await uploadOnCloudinary(imageLoacalPath)
    if(!imageUploadedUrl)
    {
        throw new ApiError(400,"Image cannot be uploaded.")
    }

    //call for checking 
    const result="say the result here"

    const detetcion=await Detection.create({
        imageUploadedUrl,result
    })

    const checkedImage=await Detection.findById(detection._id)
    if(!checkedImage){
        throw new ApiError(500, "Something went wrong while registering the user")
    }

    // return the details of the detection

    const details=await LeavesData.findOne({ name: result })
    if(!details){
        throw new ApiError(500,"we dont have data for this entry.")
    }

    return req.status(201).json(
        new ApiResponse(200,details,"Your result.")
    )

})
export {detection}