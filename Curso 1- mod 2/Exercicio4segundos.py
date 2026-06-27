segs_str = input("Por favor, entre com o número de segundos que deseja converter: ")
segs_total = int(segs_str)

dias = segs_total // 86400
segs_restantes = segs_total % 86400
horas = segs_restantes // 3600
segs_restantes_min = segs_restantes % 3600
minutos = segs_restantes_min // 60
segs_restantes_final = segs_restantes_min % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segs_restantes_final,"segundos.")