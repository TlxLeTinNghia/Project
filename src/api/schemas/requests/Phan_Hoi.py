from pydantic import BaseModel , Field, validator

class PhanHoiRequest(BaseModel):
    noi_dung: str = Field(
        ...,
        min_length=5,
        max_length=1000,
    )
    @validator("noi_dung")
    def noi_dung_hop_le(cls, v):
        if not v.strip():
            raise ValueError("Nội dung phản hồi không được để trống")
        return v