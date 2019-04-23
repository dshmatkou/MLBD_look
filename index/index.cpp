#include "index.h"
#include <iostream>


int SmallWorldIndex::AddItem(const std::string &key, const std::vector<float> &embedding) {
    if (embedding.size() != Dim)
        return 1;

    auto item = IndexItem(key, embedding);

    std::vector<int> itemIds;
    FindKNearest(GraphConnectivity, embedding, itemIds);
    item.Id = Graph.size();

    for (const auto& id : itemIds) {
        item.Friends.push_back(id);
        Graph[id].Friends.push_back(item.Id);
    }

    Graph.push_back(item);
    return 0;
}


void SmallWorldIndex::GetKeyValue(const int& id, std::string& key, std::vector<float>& embedding) {
    auto item = Graph[id];

    key = item.Key;
    embedding = item.Embedding;
}


void SmallWorldIndex::FindKNearest(const int& k, const std::vector<float>& embedding, std::vector<int>& ids) {
    // insert first k or size() items
    auto mark = std::unordered_set<int>();

    for (int i = 0; i < k && i < Graph.size(); ++i) {
        ids.push_back(i);
        mark.insert(i);
    }

    if (k >= Graph.size()) {
        return;
    }

    for (int newItem = 0; newItem != -1;) {
        // find item which will be changed if nearest found
        int maxItemIndex = 0;
        double maxDistance = -1;
        for (int i = 0; i < ids.size(); ++i) {
            double tempDistance = Graph[ids[i]].GetSquareDistance(embedding);
            if (tempDistance > maxDistance) {
                maxItemIndex = i;
                maxDistance = tempDistance;
            }
        }

        // find item nearest than maxItem
        newItem = -1;
        double newDistance = maxDistance;
        for (const auto& item : ids) {
            for (const auto& candidate : Graph[item].Friends) {
                double tempDistance = Graph[candidate].GetSquareDistance(embedding);
                if (mark.count(candidate) == 0 && tempDistance < newDistance) {
                    newDistance = tempDistance;
                    newItem = candidate;
                }
            }
        }

        if (newItem != -1) {
            ids[maxItemIndex] = newItem;
            mark.insert(newItem);
        }
    }
}
