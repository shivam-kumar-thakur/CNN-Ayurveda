import mongoose from "mongoose";

const leavesData=new mongoose.Schema({
    name:{
        type:String,
        required:true,
        trim:true
    },
    uses:{
        type:String,
    },
    physicalIdentification:{
        type:String,
    },
    toxicity:{type:String,},
    plantsWithSimilarProperties:{type:String,}
},{
    timestamps: true
})

export const LeavesData=mongoose.Model("LeavesData",leavesData)