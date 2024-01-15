import mongoose from "mongoose";

const detectSchema = new mongoose.Schema({
    fileUrl: {
        type: String,
        required: true
    },
    fastAPIResponse: {
        type: String,
        required: true
    }
},{
    timestamps: true
});

// Correct usage: mongoose.model
export const Detection = mongoose.model("Detection", detectSchema);
