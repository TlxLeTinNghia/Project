from fastapi import APIRouter, Depends, status

from api.controllers.Phan_Hoi_controller import PhanHoiController
from api.schemas.requests.Phan_Hoi import PhanHoiRequest
from api.schemas.responses.Phan_Hoi import PhanHoiResponse
from services.Phan_Hoi_Nguoi_Dung import PhanHoiUseCase
from infrastructure.repositories.Bao_Cao_repo import BaoCaoRepository
from infrastructure.repositories.Phan_Hoi_repo import PhanHoiRepository

router = APIRouter(prefix="/bao_cao",tags=["BaoCao"])

def get_phan_hoi_controller():
    return PhanHoiController(
        PhanHoiUseCase(
            BaoCaoRepository(),
            PhanHoiRepository()
        )
    )

@router.post("/phan_hoi",response_model=PhanHoiResponse,status_code=201)
def phan_hoi(
    id_bao_cao: str,
    yeu_cau: PhanHoiRequest,
    controller: PhanHoiController = Depends(get_phan_hoi_controller)
):
    bao_cao = BaoCaoRepository().get_by_id(id_bao_cao)
    return controller.phan_hoi(
        bao_cao=bao_cao,
        request=yeu_cau
    )
