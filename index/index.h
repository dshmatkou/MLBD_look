#include <vector>
#include <string>
#include <unordered_set>
#include "index_item.h"


#ifndef INDEX_H
#define INDEX_H

class SmallWorldIndex
{
private:
    std::vector<IndexItem> Graph;
    int Dim;
    int GraphConnectivity;

public:
    SmallWorldIndex()
        : Dim(), GraphConnectivity(), Graph()
    {}

    SmallWorldIndex(int dim, int graphConnectivity)
        : Dim(dim), GraphConnectivity(graphConnectivity), Graph()
    {}

    int GetDim() {
        return Dim;
    }

    int AddItem(const std::string& key, const std::vector<float>& embedding);
    void FindKNearest(const int& k, const std::vector<float>& embedding, std::vector<int>& ids);
    void GetKeyValue(const int& id, std::string& key, std::vector<float>& embedding);
};

#endif //INDEX_H
