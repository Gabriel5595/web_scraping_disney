def define_land(park, attraction_name):
    
    # Lands MK
    main_street_usa = ["Meet Mickey at Town Square Theater"]
    adventureland = ["Jungle Cruise", "The Magic Carpets of Aladdin", "Pirates of the Caribbean"]
    frontierland = ["Big Thunder Mountain Railroad", "Tiana's Bayou Adventure"]
    liberty_square = ["Haunted Mansion"]
    fantasyland = ["The Barnstormer", "Dumbo the Flying Elephant", "Enchanted Tales with Belle", "it's a small world", "Mad Tea Party", "The Many Adventures of Winnie the Pooh", "Meet Ariel at Her Grotto", "Meet Cinderella and a Visiting Princess at Princess Fairytale Hall", "Meet Daring Disney Pals as Circus Stars at Pete's Silly Side Show", "Meet Dashing Disney Pals as Circus Stars at Pete’s Silly Side Show", "Meet Princess Tiana and a Visiting Princess at Princess Fairytale Hall", "Mickey's PhilharMagic", "Peter Pan's Flight", "Prince Charming Regal Carrousel", "Seven Dwarfs Mine Train", ]
    tomorrowland = ["Astro Orbiter", "Monsters Inc. Laugh Floor", "Buzz Lightyear's Space Ranger Spin", "Space Mountain", "Tomorrowland Speedway", "Tomorrowland Transit Authority PeopleMover", "TRON Lightcycle / Run", "Under the Sea ~ Journey of The Little Mermaid"]
    
    # Lands HS
    hollywood_boulevard = ["Mickey & Minnie's Runaway Railway"]
    echo_lake = ["Meet Olaf at Celebrity Spotlight", "Star Tours – The Adventures Continue"]
    commissary_lane = ["Meet Disney Stars at Red Carpet Dreams"]
    grand_avenue = ["Muppet*Vision 3D"]
    galaxys_edge = ["Millennium Falcon: Smugglers Run", "Star Wars: Rise of the Resistance"]
    toy_story_land = ["Alien Swirling Saucers", "Slinky Dog Dash", "Toy Story Mania!"]
    pixar_plaza = ["Meet Edna Mode at the Edna Mode Experience"]
    animation_courtyard = ["Star Wars Launch Bay: Meet Chewbacca"]
    sunset_boulevard = ["Rock 'n' Roller Coaster Starring Aerosmith","The Twilight Zone Tower of Terror"]
    
    # Lands EPCOT
    world_celebration = ["Journey Into Imagination With Figment", "Meet Beloved Disney Pals at Mickey & Friends", "Spaceship Earth"]
    world_discovery = ["Guardians of the Galaxy: Cosmic Rewind", "Mission: SPACE"]
    world_nature = ["Living with the Land", "The Seas with Nemo & Friends", "Soarin'"]
    world_showcase = ["Frozen Ever After", "Gran Fiesta Tour", "Meet Anna and Elsa at Royal Sommerhus", "Remy's Ratatouille Adventure"]
    
    # Lands AK
    discovery_island = ["It's Tough to be a Bug!", "Meet Favorite Disney Pals at Adventurers Outpost"]
    pandora = ["Avatar Flight of Passage", "Na'vi River Journey"]
    africa = ["Kilimanjaro Safaris"]
    asia = ["Expedition Everest", "Kali River Rapids"]
    dinoland_usa = ["DINOSAUR", "TriceraTop Spin"]
    
    if park == "Magic Kingdom":
        if attraction_name in main_street_usa:
            return "Main Street USA"
        elif attraction_name in adventureland:
            return "Adventureland"
        elif attraction_name in frontierland:
            return "Frontierland"
        elif attraction_name in liberty_square:
            return "Liberty Square"
        elif attraction_name in fantasyland:
            return "Fantasyland"
        elif attraction_name in tomorrowland:
            return "Tomorrowland"
        else:
            return "Área não encontrada"
    elif park == "Disney's Hollywood Studios": 
        if attraction_name in hollywood_boulevard:
            return "Hollywood Boulevard"
        elif attraction_name in echo_lake:
            return "Echo Lake"
        elif attraction_name in commissary_lane:
            return "Commissary Lane"
        elif attraction_name in grand_avenue:
            return "Grand Avenue"
        elif attraction_name in galaxys_edge:
            return "Star Wars: Galaxy's Edge"
        elif attraction_name in toy_story_land:
            return "Toy Story Land"
        elif attraction_name in pixar_plaza:
            return "Pixar Plaza"
        elif attraction_name in animation_courtyard:
            return "Animation Courtyard"
        elif attraction_name in sunset_boulevard:
            return "Sunset Boulevard"
        else:
            return "Área não encontrada"
    elif park == "Epcot": 
        if attraction_name in world_celebration:
            return "World Celebration"
        elif attraction_name in world_discovery:
            return "World Discovery"
        elif attraction_name in world_nature:
            return "World Nature"
        elif attraction_name in world_showcase:
            return "World Showcase"
        else:
            return "Área não encontrada"
    elif park == "Disney's Animal Kingdom": 
        if attraction_name in discovery_island:
            return "Discovery Island"
        elif attraction_name in pandora:
            return "Pandora - The World of Avatar"
        elif attraction_name in africa:
            return "Africa"
        elif attraction_name in asia:
            return "Asia"
        elif attraction_name in dinoland_usa:
            return "Dinoland USA"
        else:
            return "Área não encontrada"
    else:
        return "Parque não encontrado"