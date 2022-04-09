# https://www.bilibili.com/video/BV1t34y197tv?p=2&spm_id_from=pageDriver

dog = {
    "name":"mjj",
    "d_type":"京巴",
    "attack_val":30
}
attack_vals = {
    "京巴":30,
    "藏獒":80,
}

def dog(name, d_type):
    data = {
        "name": "mjj",
        "d_type": "京巴",
        "life_val":100
    }
    if d_type in attack_vals:
        data["attack_val"] = attack_vals[d_type]
    else:
        data["attack_val"] = 15

    def dog_bite(person_obj):
        person_obj["life_val"] -= data["attack_val"]  # 执行咬人动作
        print("狗[%s]咬了人[%s]一口，人掉了[%s],还有血量[%s]..." % (data['name'],
                                                      person_obj['name'], data["attack_val"],
                                                      person_obj["life_val"]))
    data["bite"] = dog_bite #　保证从函数外可以调用
    return data


def person(name, age):
    data = {
        "name":name,
        "age":age,
        "life_val":100
    }
    if age > 18:
        data["attack_val"] = 50
    else:
        data["attack_val"] = 30

    def beat(dog_obj):
        dog_obj["life_val"] -= data["attack_val"]
        print("人[%s]打了狗[%s]一棒，狗掉血[%s]m还有血量[%s]" % (data['name'], dog_obj['name'],
                                                   data["attack_val"],
                                                   dog_obj["life_val"]
                                                   ))
    data["beat"] = beat
    return data


d1 = dog("mjj", "京巴")
d2 = dog("mjj2", "藏獒")

p1 = person("Alex", 22)

d1["bite"](p1) # 咬人
d1["bite"](p1) # 咬人
d1["bite"](p1) # 咬人
p1["beat"](d1) # 打狗