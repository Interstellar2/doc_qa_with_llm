## Step1：安装python依赖包

搭建虚拟环境

```
cd doc_qa_with_llm
python -m venv myvenv
```

myvenv：要生成的虚拟环境名

在虚拟环境中安装依赖包

```
cd doc_qa_with_llm
source myvenv/bin/activate
pip install -r requirements.txt
```


## Step2：通过docker安装和启动ElasticSearch和Milvus

```
cd doc_qa_with_llm/docker

docker-compose -f docker-compose-es.yml up
docker-compose -f docker-compose-milvuw.yml up
```

## Step3：启动web服务或启动gradio服务

启动web服务

```
python server.py
```

启动gradio服务

```
python server_gradio.py
```
