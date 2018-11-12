# monitor
---
> diretory

```
- monitor/          # main
  - __init__.py     # flask app init
  - apps/           # app directory
    - monitor_app/  # monitor app
      - models.py
      - urls.py
      - views.py
  - utils/          # app util diretory
  - static/         # statics diretory
  - templates/      # templates diretory
  - test/
    - test_db.py    # test Flask-SQLAlchemy module
```

>Usage

```
1.git clone
2.cd monitor/
3.pip install -r requirements.txt
4.export FLASK_APP=monitor
5.flask run --host 127.0.0.1 --port 5001
```
---

> bug

1.<s>时间不对</s> fixed : 改为js获取当前时间
---
> 例图(服务器太稳定了@_@)

![memory](/monitor/statics/memory.png)
> local_server_memory_image (O_O)

![memory](/monitor/statics/local_pc_memory.png)

