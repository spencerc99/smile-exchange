import osxphotos
import datetime
import json

DATABASE_FILE = 'photos.json'
PEOPLE_FILE = 'people.json'

def main():

    photosdb = osxphotos.PhotosDB()
    print(f"db file = {photosdb.db_path}")
    print(f"db version = {photosdb.db_version}")

    print(photosdb.keywords)
    print(photosdb.persons)
    with open(PEOPLE_FILE, 'w') as f:
        json.dump(photosdb.persons, f, indent=4)

    print(photosdb.keywords_as_dict)
    print(photosdb.persons_as_dict)

    # find all photos with Keyword = Kids and containing person Katie
    photos = photosdb.photos(albums=["photo a day"], from_date=datetime.datetime(2021, 1, 1), to_date=datetime.datetime(2021, 12, 31))

    photo_data = []
    for p in sorted(photos, key=lambda x: x.date):
        # only care about those with people
        if not p.persons:
            continue

        photo_data.append({
            "uuid": p.uuid,
            "filename": p.filename,
            "date": p.date.strftime("%Y-%m-%d"),
            "description": p.description,
            "keywords": p.keywords,
            "albums": p.albums,
            "persons": p.persons,
            "path": p.path,
        })

    print ("Exporting {} photos".format(len(photo_data)))

    with open(DATABASE_FILE, 'w') as f:
        json.dump(photo_data, f, indent=4)

# TODO: get from and end date
if __name__ == "__main__":
    main()
