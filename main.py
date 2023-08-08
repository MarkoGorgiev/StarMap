import os

from fastapi import FastAPI
import uvicorn

from models.genrate_sky_chart import DateTimeLocation

app = FastAPI()


@app.post('/generate')
def generate_chart(date_time_location: DateTimeLocation):
    date_time_location.create_star_chart()
    # TODO return the chart that we are creating to the frontend
    return None


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', '8000')))
    # call the above function with a given location and timestamp

