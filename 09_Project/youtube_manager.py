import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print('\n')
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f'{index}. {video['name']}, Duration: {video['time']}')
    print('\n')
    print("*" * 70)
    # for vid in videos:
    #     print(vid)

def add_video(videos):
    name = input('Enter video name: ')
    time = input('Enter video time: ')
    videos.append({'name': name, 'time' : time})
    save_data_helper(videos)


def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos = load_data()

    while True:
        print('\n Youtube  Manager | choose an option ')
        print('1. List all Youtube Videos ')
        print('2. Add a Youtube Video ')
        print('3. Update a Youtube Video Details')
        print('4. Delete a video ')
        print('5. Exit the App')

        choice = input('Enter the choice: ')

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                add_video(videos)

if __name__ == '__main__':
    main()