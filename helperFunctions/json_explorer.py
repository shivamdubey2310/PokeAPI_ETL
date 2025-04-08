def json_describe(json_data):
    count = 0
    # Define column widths
    index_width = 5
    column_width = 25
    main_type_width = 20
    sub_type_width = 25
    sub_sub_type_width = 30
    sub_sub_sub_type_width = 35

    # Header
    header = (
        "Index".ljust(index_width) +
        "Column".ljust(column_width) +
        "Main Type".center(main_type_width) +
        "Sub Type".center(sub_type_width) +
        "Sub Sub Type".center(sub_sub_type_width) +
        "Sub Sub Sub Type".center(sub_sub_sub_type_width)
    )
    print(header)
    print("-" * (index_width + column_width + main_type_width + sub_type_width +
                 sub_sub_type_width + sub_sub_sub_type_width))

    for key, value in json_data.items():
        index = str(count).ljust(index_width)
        column_name = key.ljust(column_width)

        # Default values
        main_type = str(type(value)).center(main_type_width)
        sub_type = "".center(sub_type_width)
        sub_sub_type = "".center(sub_sub_type_width)
        sub_sub_sub_type = "".center(sub_sub_sub_type_width)

        # Dive into nested structures
        if isinstance(value, (list, tuple)):
            main_type = str(type(value)).center(main_type_width)
            if value:
                level_1 = value[0]
                sub_type = str(type(level_1)).center(sub_type_width)

                # Sub Sub Type
                if isinstance(level_1, dict) and level_1:
                    level_2 = next(iter(level_1.values()))
                    sub_sub_type = str(type(level_2)).center(sub_sub_type_width)

                    # Sub Sub Sub Type
                    if isinstance(level_2, dict) and level_2:
                        level_3 = next(iter(level_2.values()))
                        sub_sub_sub_type = str(type(level_3)).center(sub_sub_sub_type_width)
                    elif isinstance(level_2, (list, tuple)) and level_2:
                        sub_sub_sub_type = str(type(level_2[0])).center(sub_sub_sub_type_width)
                    else:
                        sub_sub_sub_type = "N/A".center(sub_sub_sub_type_width)

                elif isinstance(level_1, (list, tuple)) and level_1:
                    level_2 = level_1[0]
                    sub_sub_type = str(type(level_2)).center(sub_sub_type_width)

                    if isinstance(level_2, (list, tuple)) and level_2:
                        sub_sub_sub_type = str(type(level_2[0])).center(sub_sub_sub_type_width)
                    elif isinstance(level_2, dict) and level_2:
                        level_3 = next(iter(level_2.values()))
                        sub_sub_sub_type = str(type(level_3)).center(sub_sub_sub_type_width)
                    else:
                        sub_sub_sub_type = "N/A".center(sub_sub_sub_type_width)
                else:
                    sub_sub_type = "N/A".center(sub_sub_type_width)
                    sub_sub_sub_type = "N/A".center(sub_sub_sub_type_width)
            else:
                sub_type = "Empty List/Tuple".center(sub_type_width)
                sub_sub_type = "N/A".center(sub_sub_type_width)
                sub_sub_sub_type = "N/A".center(sub_sub_sub_type_width)

        print(index + column_name + main_type + sub_type + sub_sub_type + sub_sub_sub_type)
        count += 1
