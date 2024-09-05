## Create Env
- Using python 3.11.9

- create venv
```
python -m venv your_venv_name
```

- activate venv

```
source venv/bin/activate
```

- intall requirement

```
pip install -r requirements.txt
```
## first data model

      text_input intents 
0            Hai   salam  
1             Hi   salam  
2           Halo   salam 
3      Apa Kabar   salam  
4   Selamat Pagi   salam  
5  Selamat Siang   salam  
6  Selamat Malam   salam  
7          Salam   salam      
8           Ping   salam          
9              P   salam

## preprocessed

      text_input intents text_input_prep
0            Hai   salam             hai
1             Hi   salam              hi
2           Halo   salam            halo
3      Apa Kabar   salam       apa kabar
4   Selamat Pagi   salam    selamat pagi
5  Selamat Siang   salam   selamat siang
6  Selamat Malam   salam   selamat malam
7          Salam   salam           salam
8           Ping   salam            ping
9              P   salam               p