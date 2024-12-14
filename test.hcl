variable "typless_variable" {}
variable "structural-types" {
  type = object({
    nested: object({
      can-be-nested = bool
    }),
    tuple: tuple([int, string])
  })

  default = {
    nested = { can-be-nested = true }
    tuple = [16, "cm"]
  }
}

# /* 
#  * COLLECTIONS:
#  * * LIST
#  * * MAP
#  * * SET
#  */

variable "list" {
  type = list(string)
  default = ["Hello", ",", "world", "!"]
}

variable "map" {
  type = map(any)
  default = {
    red = "#ff0000"
    green = "#00ff00"
    blue = "#0000ff"
  }
}

variable "set" {
  type = set(string)
  default = ["red", "blue", "green"]
}
