import mongoose from "mongoose";

const leavesData=new mongoose.Schema({
    name:{},
    uses:{},
    physicalIdentification:{},
    toxicity:{},
    plantsWithSimilarProperties:{}
})

export const LeavesData=mongoose.Model("LeavesData",leavesData)