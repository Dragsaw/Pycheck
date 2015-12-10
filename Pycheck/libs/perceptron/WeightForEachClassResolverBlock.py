class WeightForEachClassResolverBlock(object):

    def __init__(self, **kwargs):
        self._addressables = []
        self._classes = { 0: '' }
        self.weights = dict()
        self.step = 1
        self.threshold = 1
        self._outputs = []

    def resolve_class(self):
        self._outputs.clear()
        result = dict.fromkeys(self.weights.keys(), 0)
        for i in range(0, len(self._addressables)):
            output = self._addressables[i].get_output(self.threshold)
            self._outputs.append(output)
            for w in self.weights:
                result[w] += output * self.weights[w][i]
        answer_index = max(result, key=result.get)
        return self._classes[answer_index]

    def calibrate(self, type):
        if self._classes[0] == '':
            self._classes[0] = type
            return
        if not type in self._classes.values():
            index = len(self._classes)
            self._classes[index] = type
            self.weights[index] = [index-1 for i in  range(0, len(self._addressables))]
        self.__calibrate_weights(type)

    def __calibrate_weights(self, type):
        type_index = -1
        for k, v in self._classes.items():
            if v == type:
                type_index = k
                break
        for i in range(0, len(self._outputs)):
            if self._outputs[i] == 1:
                for w in self.weights:
                    if w == type_index:
                        self.weights[w][i] += self.step
                    else:
                        self.weights[w][i] -= self.step

    @property
    def addressables(self):
        return self._addressables

    @addressables.setter
    def addressables(self, value):
        self._addressables = value
        self.weights[0] = [-1 for i in range(0, len(value))]