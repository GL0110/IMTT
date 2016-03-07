class Track:
    def __init__(self, index, instance_id, match_d_thresh,
                 sep_thresh, res_frac_multiplier):
        self.resolution_frac_multiplier = res_frac_multiplier
        self.frame_index = index
        self.birth_frame_index = index
        self.death_frame_index = 0
        self.id_num = instance_id
        self.match_distance_threshold = match_d_thresh
        self.nuke_distance_threshold = sep_thresh
        self.number_of_zombie_frames = 0
        self.is_birthable = False
        self.is_birth_frame = True

        self.model_type = "none"

    """
    Given a vector of data points and a vector of model points, use ICP to
    register the model to the data. Add registration transformation to 
    transforms vector and registration transformation from the track's birth
    frame to absolute_transforms vector
    """
    def UpdatePosition(self, data_points, current_track_points,
                       model_to_data_thresh, sep_thresh, match_d_thresh,
                       icp_iterations, icp_trans_eps, icp_euclid_dist,
                       icp_max_fit):
        self.match_distance_threshold = match_d_thresh
        self.nuke_distance_threshold = sep_thresh

        self.icp_max_iter = icp_iterations
        self.icp_transformation_epsilon = icp_trans_eps
        self.icp_max_fitness = icp_max_fit

        # Get identity of the model for this region.
        if self.frame_index == self.birth_frame_index:
            self.is_birth_frame = True
            if len(current_track_points) < 2:
                self.model_index = 0
            else:
                #TODO(carden): find model index in data points array
                #self.model_index = 
                pass
        else:
            self.is_birth_frame = False

    # Determine health of latest part of track.
    
    # Just born tracks go here:
                

    # Increment frame counter.
    self.frame_index += 1

    return data_points_reduced

                       
