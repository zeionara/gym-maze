def group(items, n_items_per_group: int):
    if len(items) <= n_items_per_group:
        return [tuple(items)]

    groups = []
    current_group = None
    for i, item in enumerate(items):
        if i % n_items_per_group == 0:
            if current_group is not None and len(current_group) > 0:
                groups.append(tuple(current_group))
            current_group = [item]
        else:
            current_group.append(item)

    if len(current_group) > 0:
        groups.append(tuple(current_group))

    return groups
