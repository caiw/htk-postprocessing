function add_category_colours_to_dendrogram(cond_perm, category_labels, category_colours)
    hold on;
    x = xlim(gca);
    y = ylim(gca);
    n_conditions = numel(category_labels);
    for condition_i = 1:n_conditions
        condition_label = category_labels(condition_i);
        plot( ...
            x(1), cond_perm(condition_i), ...
            'o', ...
            'MarkerFaceColor', category_colours(condition_label, :), ...
            'MarkerEdgeColor', 'none', ...
            'MarkerSize', 6);
    end%for:condition
end%function
