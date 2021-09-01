import pymysql
import hashlib
import jwt

secreta="my2w7wjd7yXF64FIADfJxNs1oupTGAuW"
class Token:
    def generate_token(self,username,password):
        conn = pymysql.connect(host = "bootcamp-tht.sre.wize.mx",
                              user = "secret",
                              password = "noPow3r",
                              db = "bootcamp_tht")
        cursor = conn.cursor()
        cursor.execute("select * from users where username='%s';"%username)
        info = cursor.fetchone()
        try:
            usernameb,passwordb,saltb,roleb=info
            hash_very=hashlib.sha512(password.encode()+saltb.encode()).hexdigest()
            if passwordb==hash_very:
                pl={
                    "role":roleb
                }
                token=jwt.encode(payload=pl,key=secreta)
                return token
            else:
                return 403
        except:
            return 403

class Restricted:
    def access_data(self, authorization):
        try:
            acc = jwt.decode(authorization, algorithms=["HS256"], key=secreta)
            roles = ["admin", "editor", "viewer"]
            for i in roles:
                if acc["role"] == i:
                    return "You are under protected data"
        except:
            return 403
