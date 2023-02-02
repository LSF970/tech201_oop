# Methods

# class MethodExamples:
#
#     # his_can_be_accessed_easily = "Hi, I am easily found!"
#
#     def __init__(self):
#         self.this_can_be_accessed_easily = "Hi, I am easily found!"

# x = MethodExamples()
# #
# print(x.this_can_be_accessed_easily)
# x.this_can_be_accessed_easily = "I have been changed!"
# print(x.this_can_be_accessed_easily)

# Public and Private

class MethodExamples:

    # this_can_be_accessed_easily = "Hi, here I am easily found"

    def __init__(self):
        self._this_can_be_accessed_easily = "Hi, here I am easily found"

    def __get_this_can_be_accessed_easily(self):
        return self._this_can_be_accessed_easily

    def set_this_can_be_accessed_easily(self, value_to_be_set):
        self._this_can_be_accessed_easily = value_to_be_set

x = MethodExamples()

print(x.get_this_can_be_accessed_easily())
x.set_this_can_be_accessed_easily("I have changed")
print(x.get_this_can_be_accessed_easily())
