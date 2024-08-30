def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_length = 60

    for i, item in enumerate(lst):
        if i % 20 == 0 or i == total - 1:
            progress = (i + 1) / total
            filled_length = int(bar_length * progress)
            bar = "█" * filled_length + ' ' * (bar_length - filled_length)
            percent = int(progress * 100)

            remaining_time = 1 - progress
            it = 190
            
            # Format the elapsed and remaining time as MM:SS
            progress_str = f'00:{int(progress):02}'
            remaining_str =f'00:{int(remaining_time):02}' 

            print(f'\r{percent}%|{bar}| {i + 1}/{total}', end='')
            print(f' [{progress_str}<{remaining_str}, {it:.2f}it/s]', end='')

        yield item

    print()
