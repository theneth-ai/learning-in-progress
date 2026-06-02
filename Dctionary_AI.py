
ai_companies = {1: "Google",
                2: "OpenAI", 
                3: "Meta", 
                4: "Microsoft",
                5: "Nvidia",
                6:"Apple"}
ceos = {"Google": "Sundar Pichai", 
        "OpenAI": "Sam Altman",
        "Meta": "Mark Zuckerberg",
        "Microsoft": "Satya Nadella",
        "Nvidia": "Jensen Huang"}

for rank, name in ai_companies.items():
    ceo_name = ceos.get(name, "Not Found!")
    print(f"Rank {rank} belongs to {name} \t| Chief Executive Officer: {ceo_name}")


