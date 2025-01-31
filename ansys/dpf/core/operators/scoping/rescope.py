"""
rescope
=======
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "scoping" category
"""

class rescope(Operator):
    """Rescope a field on the given scoping. If an id does not exists in the original field, default value (in 2) is used if defined.

      available inputs:
        - fields (FieldsContainer, Field)
        - mesh_scoping (Scoping, list)
        - default_value (float, list)

      available outputs:
        - fields (FieldsContainer ,Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.scoping.rescope()

      >>> # Make input connections
      >>> my_fields = dpf.FieldsContainer()
      >>> op.inputs.fields.connect(my_fields)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_default_value = float()
      >>> op.inputs.default_value.connect(my_default_value)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.scoping.rescope(fields=my_fields,mesh_scoping=my_mesh_scoping,default_value=my_default_value)

      >>> # Get output data
      >>> result_fields = op.outputs.fields()"""
    def __init__(self, fields=None, mesh_scoping=None, default_value=None, config=None, server=None):
        super().__init__(name="Rescope", config = config, server = server)
        self._inputs = InputsRescope(self)
        self._outputs = OutputsRescope(self)
        if fields !=None:
            self.inputs.fields.connect(fields)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if default_value !=None:
            self.inputs.default_value.connect(default_value)

    @staticmethod
    def _spec():
        spec = Specification(description="""Rescope a field on the given scoping. If an id does not exists in the original field, default value (in 2) is used if defined.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields", type_names=["fields_container","field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh_scoping", type_names=["scoping","vector<int32>"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "default_value", type_names=["double","vector<double>"], optional=False, document="""if a the pin 2 is used, the ids not found in the fields are added with this default value""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields", type_names=["fields_container","field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "Rescope")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsRescope 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsRescope 
        """
        return super().outputs


#internal name: Rescope
#scripting name: rescope
class InputsRescope(_Inputs):
    """Intermediate class used to connect user inputs to rescope operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.rescope()
      >>> my_fields = dpf.FieldsContainer()
      >>> op.inputs.fields.connect(my_fields)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
      >>> my_default_value = float()
      >>> op.inputs.default_value.connect(my_default_value)
    """
    def __init__(self, op: Operator):
        super().__init__(rescope._spec().inputs, op)
        self._fields = Input(rescope._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields)
        self._mesh_scoping = Input(rescope._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh_scoping)
        self._default_value = Input(rescope._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._default_value)

    @property
    def fields(self):
        """Allows to connect fields input to the operator

        Parameters
        ----------
        my_fields : FieldsContainer, Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.rescope()
        >>> op.inputs.fields.connect(my_fields)
        >>> #or
        >>> op.inputs.fields(my_fields)

        """
        return self._fields

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        Parameters
        ----------
        my_mesh_scoping : Scoping, list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.rescope()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

    @property
    def default_value(self):
        """Allows to connect default_value input to the operator

        - pindoc: if a the pin 2 is used, the ids not found in the fields are added with this default value

        Parameters
        ----------
        my_default_value : float, list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.rescope()
        >>> op.inputs.default_value.connect(my_default_value)
        >>> #or
        >>> op.inputs.default_value(my_default_value)

        """
        return self._default_value

class OutputsRescope(_Outputs):
    """Intermediate class used to get outputs from rescope operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.rescope()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields = op.outputs.fields()
    """
    def __init__(self, op: Operator):
        super().__init__(rescope._spec().outputs, op)
        self.fields_as_fields_container = Output( _modify_output_spec_with_one_type(rescope._spec().output_pin(0), "fields_container"), 0, op) 
        self._outputs.append(self.fields_as_fields_container)
        self.fields_as_field = Output( _modify_output_spec_with_one_type(rescope._spec().output_pin(0), "field"), 0, op) 
        self._outputs.append(self.fields_as_field)

