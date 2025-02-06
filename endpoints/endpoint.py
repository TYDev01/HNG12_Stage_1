from fastapi import APIRouter, Query, HTTPException
from utilis.utils import is_armstrong, is_prime, is_perfect, get_fun_fact

router = APIRouter()

@router.get("/classify-number")
def generate(number: str = Query(..., description="Enter a number")):
    try:
        number = int(number)
    except ValueError:
        raise HTTPException(status_code=400, detail={"number": number, "error": True})

    properties = []

    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("even" if number % 2 == 0 else "odd")

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(abs(number))),
        "fun_fact": get_fun_fact(number)
    }
