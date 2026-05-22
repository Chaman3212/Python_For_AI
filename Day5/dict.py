info={
    "name":"chirag",
    "sec":"fc",
    "roll_no":"24"
}

print(info)
info["sec"]="Ag"
print(info)
print(info.get("name"))
print(info.update({"city":"mathura"}))