"""
unit_convert
============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "math" category
"""

class unit_convert(Operator):
    """Convert an input field/fields container or mesh of a given unit to another unit.

      available inputs:
        - entity_to_convert (Field, FieldsContainer, MeshedRegion, MeshesContainer)
        - unit_name (str)

      available outputs:
        - converted_entity (Field ,FieldsContainer ,MeshedRegion ,MeshesContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.unit_convert()

      >>> # Make input connections
      >>> my_entity_to_convert = dpf.Field()
      >>> op.inputs.entity_to_convert.connect(my_entity_to_convert)
      >>> my_unit_name = str()
      >>> op.inputs.unit_name.connect(my_unit_name)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.unit_convert(entity_to_convert=my_entity_to_convert,unit_name=my_unit_name)

      >>> # Get output data
      >>> result_converted_entity = op.outputs.converted_entity()"""
    def __init__(self, entity_to_convert=None, unit_name=None, config=None, server=None):
        super().__init__(name="unit_convert", config = config, server = server)
        self._inputs = InputsUnitConvert(self)
        self._outputs = OutputsUnitConvert(self)
        if entity_to_convert !=None:
            self.inputs.entity_to_convert.connect(entity_to_convert)
        if unit_name !=None:
            self.inputs.unit_name.connect(unit_name)

    @staticmethod
    def _spec():
        spec = Specification(description="""Convert an input field/fields container or mesh of a given unit to another unit.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "entity_to_convert", type_names=["field","fields_container","abstract_meshed_region","meshes_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "unit_name", type_names=["string"], optional=False, document="""unit as a string, ex 'm' for meter, 'Pa' for pascal,...""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "converted_entity", type_names=["field","fields_container","abstract_meshed_region","meshes_container"], optional=False, document="""the output entity is the same as the input (inplace operator)""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "unit_convert")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsUnitConvert 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsUnitConvert 
        """
        return super().outputs


#internal name: unit_convert
#scripting name: unit_convert
class InputsUnitConvert(_Inputs):
    """Intermediate class used to connect user inputs to unit_convert operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.unit_convert()
      >>> my_entity_to_convert = dpf.Field()
      >>> op.inputs.entity_to_convert.connect(my_entity_to_convert)
      >>> my_unit_name = str()
      >>> op.inputs.unit_name.connect(my_unit_name)
    """
    def __init__(self, op: Operator):
        super().__init__(unit_convert._spec().inputs, op)
        self._entity_to_convert = Input(unit_convert._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._entity_to_convert)
        self._unit_name = Input(unit_convert._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._unit_name)

    @property
    def entity_to_convert(self):
        """Allows to connect entity_to_convert input to the operator

        Parameters
        ----------
        my_entity_to_convert : Field, FieldsContainer, MeshedRegion, MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.unit_convert()
        >>> op.inputs.entity_to_convert.connect(my_entity_to_convert)
        >>> #or
        >>> op.inputs.entity_to_convert(my_entity_to_convert)

        """
        return self._entity_to_convert

    @property
    def unit_name(self):
        """Allows to connect unit_name input to the operator

        - pindoc: unit as a string, ex 'm' for meter, 'Pa' for pascal,...

        Parameters
        ----------
        my_unit_name : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.unit_convert()
        >>> op.inputs.unit_name.connect(my_unit_name)
        >>> #or
        >>> op.inputs.unit_name(my_unit_name)

        """
        return self._unit_name

class OutputsUnitConvert(_Outputs):
    """Intermediate class used to get outputs from unit_convert operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.unit_convert()
      >>> # Connect inputs : op.inputs. ...
      >>> result_converted_entity = op.outputs.converted_entity()
    """
    def __init__(self, op: Operator):
        super().__init__(unit_convert._spec().outputs, op)
        self.converted_entity_as_field = Output( _modify_output_spec_with_one_type(unit_convert._spec().output_pin(0), "field"), 0, op) 
        self._outputs.append(self.converted_entity_as_field)
        self.converted_entity_as_fields_container = Output( _modify_output_spec_with_one_type(unit_convert._spec().output_pin(0), "fields_container"), 0, op) 
        self._outputs.append(self.converted_entity_as_fields_container)
        self.converted_entity_as_meshed_region = Output( _modify_output_spec_with_one_type(unit_convert._spec().output_pin(0), "abstract_meshed_region"), 0, op) 
        self._outputs.append(self.converted_entity_as_meshed_region)
        self.converted_entity_as_meshes_container = Output( _modify_output_spec_with_one_type(unit_convert._spec().output_pin(0), "meshes_container"), 0, op) 
        self._outputs.append(self.converted_entity_as_meshes_container)

