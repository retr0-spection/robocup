import numpy as np





def _find_most_foward_players(players, num=3):
    _results = []
    x_positions = [player[0] for player in players]
    for i in range(num):
        idx = x_positions.index([max(x_positions)])
        _results.append(players[i])
        x_positions[idx] = -100

    return _results

def _find_most_open_attacking_player_pos(origin, teammates, opponent):
    possibilities = _find_most_foward_players(teammates)

    gaps = []
    for teammate in possibilities:
        if teammate[0] > origin[0]:
            gaps.append(_calculate_gap(origin, teammate, opponent))

    #choose maximum gap in front of origin
    
    try:
        result = teammates[gaps.index(max(gaps))]
    except ValueError as e:
        result = None

    return result


def _calculate_gap(origin, teammate, opponent):
    # Define points
    p1 =origin # Player 1 position
    p2 = teammate  # Player 2 position
    p3 = opponent  # Player 3 position

    # Calculate vectors from p1 to p2 and p1 to p3
    v12 = p2 - p1
    v13 = p3 - p1

    # Calculate the cosine of the angle between v12 and v13
    cos_theta = np.dot(v12, v13) / (np.linalg.norm(v12) * np.linalg.norm(v13))

    # Calculate the angle in degrees
    theta_deg = np.degrees(np.arccos(cos_theta))
    print('theta', theta_deg)

    return theta_deg


def _find_closest_pair(origin, teammates):
	origin = np.array(origin)
	teammates = np.array(teammates)
	distances = [euclidean_distance(origin, teammate) if (teammate[0] == origin[0] and teammate[1] == origin[1]) else 1000 for teammate in teammates]
	_ = min(distances)
	idx = distances.index(_)
	candidate = teammates[idx]
	#mate is ahead in the field
	if candidate[0] >= origin[0]:
		return candidate
	else:
		return None