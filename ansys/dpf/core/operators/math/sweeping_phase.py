"""
sweeping_phase
==============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "math" category
"""

class sweeping_phase(Operator):
    """Shift the phase of a real and an imaginary fields (in 0 and 1) of a given angle (in 3) of unit (in 4).

      available inputs:
        - real_field (Field, FieldsContainer)
        - imaginary_field (Field, FieldsContainer)
        - angle (float)
        - unit_name (str)
        - abs_value (bool)
        - imaginary_part_null (bool)

      available outputs:
        - field (Field)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.sweeping_phase()

      >>> # Make input connections
      >>> my_real_field = dpf.Field()
      >>> op.inputs.real_field.connect(my_real_field)
      >>> my_imaginary_field = dpf.Field()
      >>> op.inputs.imaginary_field.connect(my_imaginary_field)
      >>> my_angle = float()
      >>> op.inputs.angle.connect(my_angle)
      >>> my_unit_name = str()
      >>> op.inputs.unit_name.connect(my_unit_name)
      >>> my_abs_value = bool()
      >>> op.inputs.abs_value.connect(my_abs_value)
      >>> my_imaginary_part_null = bool()
      >>> op.inputs.imaginary_part_null.connect(my_imaginary_part_null)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.sweeping_phase(real_field=my_real_field,imaginary_field=my_imaginary_field,angle=my_angle,unit_name=my_unit_name,abs_value=my_abs_value,imaginary_part_null=my_imaginary_part_null)

      >>> # Get output data
      >>> result_field = op.outputs.field()"""
    def __init__(self, real_field=None, imaginary_field=None, angle=None, unit_name=None, abs_value=None, imaginary_part_null=None, config=None, server=None):
        super().__init__(name="sweeping_phase", config = config, server = server)
        self._inputs = InputsSweepingPhase(self)
        self._outputs = OutputsSweepingPhase(self)
        if real_field !=None:
            self.inputs.real_field.connect(real_field)
        if imaginary_field !=None:
            self.inputs.imaginary_field.connect(imaginary_field)
        if angle !=None:
            self.inputs.angle.connect(angle)
        if unit_name !=None:
            self.inputs.unit_name.connect(unit_name)
        if abs_value !=None:
            self.inputs.abs_value.connect(abs_value)
        if imaginary_part_null !=None:
            self.inputs.imaginary_part_null.connect(imaginary_part_null)

    @staticmethod
    def _spec():
        spec = Specification(description="""Shift the phase of a real and an imaginary fields (in 0 and 1) of a given angle (in 3) of unit (in 4).""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "real_field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 1 : PinSpecification(name = "imaginary_field", type_names=["field","fields_container"], optional=False, document="""field or fields container with only one field is expected"""), 
                                 2 : PinSpecification(name = "angle", type_names=["double"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "unit_name", type_names=["string"], optional=False, document="""String Unit"""), 
                                 4 : PinSpecification(name = "abs_value", type_names=["bool"], optional=False, document=""""""), 
                                 5 : PinSpecification(name = "imaginary_part_null", type_names=["bool"], optional=False, document="""if the imaginary part field is empty and this pin is true, then the imaginary part is supposed to be 0 (default is false)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field", type_names=["field"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "sweeping_phase")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsSweepingPhase 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsSweepingPhase 
        """
        return super().outputs


#internal name: sweeping_phase
#scripting name: sweeping_phase
class InputsSweepingPhase(_Inputs):
    """Intermediate class used to connect user inputs to sweeping_phase operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.sweeping_phase()
      >>> my_real_field = dpf.Field()
      >>> op.inputs.real_field.connect(my_real_field)
      >>> my_imaginary_field = dpf.Field()
      >>> op.inputs.imaginary_field.connect(my_imaginary_field)
      >>> my_angle = float()
      >>> op.inputs.angle.connect(my_angle)
      >>> my_unit_name = str()
      >>> op.inputs.unit_name.connect(my_unit_name)
      >>> my_abs_value = bool()
      >>> op.inputs.abs_value.connect(my_abs_value)
      >>> my_imaginary_part_null = bool()
      >>> op.inputs.imaginary_part_null.connect(my_imaginary_part_null)
    """
    def __init__(self, op: Operator):
        super().__init__(sweeping_phase._spec().inputs, op)
        self._real_field = Input(sweeping_phase._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._real_field)
        self._imaginary_field = Input(sweeping_phase._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._imaginary_field)
        self._angle = Input(sweeping_phase._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._angle)
        self._unit_name = Input(sweeping_phase._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._unit_name)
        self._abs_value = Input(sweeping_phase._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._abs_value)
        self._imaginary_part_null = Input(sweeping_phase._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self._imaginary_part_null)

    @property
    def real_field(self):
        """Allows to connect real_field input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_real_field : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.sweeping_phase()
        >>> op.inputs.real_field.connect(my_real_field)
        >>> #or
        >>> op.inputs.real_field(my_real_field)

        """
        return self._real_field

    @property
    def imaginary_field(self):
        """Allows to connect imaginary_field input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_imaginary_field : Field, FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.sweeping_phase()
        >>> op.inputs.imaginary_field.connect(my_imaginary_field)
        >>> #or
        >>> op.inputs.imaginary_field(my_imaginary_field)

        """
        return self._imaginary_field

    @property
    def angle(self):
        """Allows to connect angle input to the operator

        Parameters
        ----------
        my_angle : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.sweeping_phase()
        >>> op.inputs.angle.connect(my_angle)
        >>> #or
        >>> op.inputs.angle(my_angle)

        """
        return self._angle

    @property
    def unit_name(self):
        """Allows to connect unit_name input to the operator

        - pindoc: String Unit

        Parameters
        ----------
        my_unit_name : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.sweeping_phase()
        >>> op.inputs.unit_name.connect(my_unit_name)
        >>> #or
        >>> op.inputs.unit_name(my_unit_name)

        """
        return self._unit_name

    @property
    def abs_value(self):
        """Allows to connect abs_value input to the operator

        Parameters
        ----------
        my_abs_value : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.sweeping_phase()
        >>> op.inputs.abs_value.connect(my_abs_value)
        >>> #or
        >>> op.inputs.abs_value(my_abs_value)

        """
        return self._abs_value

    @property
    def imaginary_part_null(self):
        """Allows to connect imaginary_part_null input to the operator

        - pindoc: if the imaginary part field is empty and this pin is true, then the imaginary part is supposed to be 0 (default is false)

        Parameters
        ----------
        my_imaginary_part_null : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.sweeping_phase()
        >>> op.inputs.imaginary_part_null.connect(my_imaginary_part_null)
        >>> #or
        >>> op.inputs.imaginary_part_null(my_imaginary_part_null)

        """
        return self._imaginary_part_null

class OutputsSweepingPhase(_Outputs):
    """Intermediate class used to get outputs from sweeping_phase operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.sweeping_phase()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field = op.outputs.field()
    """
    def __init__(self, op: Operator):
        super().__init__(sweeping_phase._spec().outputs, op)
        self._field = Output(sweeping_phase._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator


        Returns
        ----------
        my_field : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.sweeping_phase()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field() 
        """
        return self._field
