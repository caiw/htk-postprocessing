% Produces sliding-window-matched plots for the instances of each phone for
% each word.
function [feature_models] = feature_activations()

    load_dir  = fullfile('/Users', 'cai', 'Desktop', 'scratch', 'py_out');

    segmentations = load(fullfile(load_dir, 'triphone_boundaries.mat'));
    segmentations = orderfields(segmentations);
    words = fieldnames(segmentations);

    phone_models = phone_activations();
    phone_models = orderfields(phone_models);
    phones = fieldnames(phone_models);
    
    feature_matrix = phonetic_feature_matrix();
    features = fieldnames(feature_matrix);
    
    n_words    = numel(words);
    n_features = numel(features);
    
    word_length = size(phone_models.(phones{1}), 2);
    
    feature_models = struct();
    
    for feature_i = 1:n_features
        feature = features{feature_i};
        
        % the indices of the phones which possess this feature
        phone_is_this_feature = find(feature_matrix.(feature));
        
        %   ,Will index the phone indices
        for phone_is_i = 1:numel(phone_is_this_feature)
            % Index of the phone
            phone_i = phone_is_this_feature(phone_is_i);
            phone = phones{phone_i};
            
            if phone_is_i == 1
                % For the first one we just grab it
                feature_model = phone_models.(phone);
            else
                % For the others we add it on
                feature_model = feature_model + phone_models.(phone);
            end
        end
        
        % store it for this feature
        feature_models.(feature) = feature_model;
        
    end
    
end%function
