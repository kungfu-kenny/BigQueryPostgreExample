FROM gcr.io/dataflow-templates-base/python3-template-launcher-base

ARG WORKDIR=/dataflow/template
RUN mkdir -p ${WORKDIR}
WORKDIR ${WORKDIR}

ENV JSON_NAME='your json name'

ENV HOST='localhost'
ENV USER_DB='postgres user'
ENV PORT='5432'
ENV DATABASE='postgres db'
ENV PASSWORD='postgres password'

ENV PROJECT_ID='your project'
ENV DATASET='your dataset'
ENV TABLE='your table'
ENV BUCKET='your bucket'

COPY . .

ENV FLEX_TEMPLATE_PYTHON_PY_FILE="${WORKDIR}/develop_send.py"

RUN pip install pandas sqlalchemy python-dotenv psycopg2-binary
RUN pip install apache-beam[gcp]