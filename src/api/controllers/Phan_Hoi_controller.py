from fastapi import HTTPException, status

from services.Phan_Hoi_Nguoi_Dung import PhanHoiUseCase
from api.schemas.responses.Phan_Hoi import PhanHoiResponse
from api.schemas.requests.Phan_Hoi import PhanHoiRequest




class PhanHoiController:
    def __init__(self, phan_hoi: PhanHoiUseCase):
        self.ser_phan_hoi = phan_hoi

    def phan_hoi(
        self,
        id_bao_cao: int,
        request: PhanHoiRequest
    ) -> PhanHoiResponse:
        try:
            phan_hoi = self.ser_phan_hoi.execute(
                id_bao_cao=id_bao_cao,
                noi_dung=request.noi_dung
            )

            return PhanHoiResponse(
                id_phan_hoi=phan_hoi.id,
                id_bao_cao=id_bao_cao,
                noi_dung=phan_hoi.noi_dung,
                thoi_gian_phan_hoi=phan_hoi.thoi_gian
            )

        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )