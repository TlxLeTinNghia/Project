from pydantic import BaseModel
from datetime import datetime

class PhanHoiResponse(BaseModel):
    id_phan_hoi : str 
    id_bao_cao: str 
    noi_dung_phan_hoi : str
    ngay_gui: datetime 
