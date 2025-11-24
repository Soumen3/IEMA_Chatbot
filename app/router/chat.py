from fastapi import APIRouter, HTTPException, Depends
from services.chat_services import generate_response
from models.response import EnquiryModel
from models.enquiry import Enquiry
from database import get_db
from sqlalchemy.orm import Session
from datetime import datetime

router = APIRouter(prefix="/chat")

@router.post("/")
async def chat(prompt: str):
    reply = await generate_response(prompt)
    return {"reply": reply}

@router.post("/submit-form")
async def submit_form(enquiry: EnquiryModel, db: Session = Depends(get_db)):
    print(f"Received enquiry: {enquiry}")
    try:
        new_enquiry = Enquiry(
            name=enquiry.name,
            email=enquiry.email,
            phone=enquiry.phone,
            option=enquiry.option,
            school_name=enquiry.school_name,
            city_state=enquiry.city_state,
            requirement=enquiry.requirement,
            query=enquiry.query,
            timestamp=datetime.now()
        )
        
        db.add(new_enquiry)
        db.commit()
        db.refresh(new_enquiry)
            
        return {"message": "Form submitted successfully", "id": new_enquiry.id}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
