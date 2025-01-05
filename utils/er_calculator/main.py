# particles = {
#     "mauvika_e": {
#         "count": 5,
#         "type": "onfield",
#         "element": "same"
#     },
#     "bennett_e": {
#         "count": 2.25,
#         "type": "off field",
#         "element": "same"
#     },
#     "bennett_e_downtime": {
#         "count": 2.25,
#         "type": "onfield",
#         "element": "same"
#     },
#     "guoba_e": {
#         "count": 8,
#         "type": "off field",
#         "element": "same"
#     },
#     "childe_e": {
#         "count": 4,
#         "type": "off field",
#         "element": "different"
#     },
# }

particles = {
    # two tap E's and half funnel rate
    "kaz_e": {
        "count": 3,
        "type": "onfield",
        "element": "different"
    },
    "kaz_e_fav": {
        "count": 3,
        "type": "onfield",
        "element": "white"
    },
    "kaz_e_downtime": {
        "count": 3,
        "type": "off field",
        "element": "different"
    },
    "kaz_e_fav_downtime": {
        "count": 3,
        "type": "off field",
        "element": "white"
    },
    "bennett_e": {
        "count": 2.25,
        "type": "off field",
        "element": "same"
    },
    # "bennett_e_downtime": {
    #     "count": 2.25,
    #     "type": "onfield",
    #     "element": "same"
    # },
    "guoba_e": {
        "count": 8,
        "type": "off field",
        "element": "same"
    },
    "childe_e": {
        "count": 4,
        "type": "off field",
        "element": "different"
    },
}

multipliers = {
    "onfield": {
        "same": 3,
        "different": 1,
        "white": 2 
    },
    "off field": {
        "same": 1.8,
        "different": 0.6,
        "white": 1.2 
    }
}

cost = 80
raw_energy = 0
for action, particle in particles.items():
    energy = particle["count"] * multipliers[particle["type"]][particle["element"]]
    print(f"{action}:", energy)
    raw_energy += energy

print("Raw Energy:", raw_energy)

er = cost / raw_energy

print("ER:", er)
