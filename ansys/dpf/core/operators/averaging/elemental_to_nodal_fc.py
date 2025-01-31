"""
elemental_to_nodal_fc
=====================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.FEMutils plugin, from "averaging" category
"""

class elemental_to_nodal_fc(Operator):
    """Transform ElementalNodal fields to Nodal fields, compute result on a given node scoping.

      available inputs:
        - fields_container (FieldsContainer)
        - mesh (MeshedRegion, MeshesContainer) (optional)
        - force_averaging (int) (optional)
        - mesh_scoping (Scoping, ScopingsContainer) (optional)

      available outputs:
        - fields_container (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.averaging.elemental_to_nodal_fc()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_force_averaging = int()
      >>> op.inputs.force_averaging.connect(my_force_averaging)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.averaging.elemental_to_nodal_fc(fields_container=my_fields_container,mesh=my_mesh,force_averaging=my_force_averaging,mesh_scoping=my_mesh_scoping)

      >>> # Get output data
      >>> result_fields_container = op.outputs.fields_container()"""
    def __init__(self, fields_container=None, mesh=None, force_averaging=None, mesh_scoping=None, config=None, server=None):
        super().__init__(name="elemental_to_nodal_fc", config = config, server = server)
        self._inputs = InputsElementalToNodalFc(self)
        self._outputs = OutputsElementalToNodalFc(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if force_averaging !=None:
            self.inputs.force_averaging.connect(force_averaging)
        if mesh_scoping !=None:
            self.inputs.mesh_scoping.connect(mesh_scoping)

    @staticmethod
    def _spec():
        spec = Specification(description="""Transform ElementalNodal fields to Nodal fields, compute result on a given node scoping.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=True, document=""""""), 
                                 2 : PinSpecification(name = "force_averaging", type_names=["int32"], optional=True, document="""averaging on nodes is used if this pin is set to 1 (default is one for integrated results and 0 for dicrete ones)"""), 
                                 3 : PinSpecification(name = "mesh_scoping", type_names=["scoping","scopings_container"], optional=True, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "elemental_to_nodal_fc")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsElementalToNodalFc 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsElementalToNodalFc 
        """
        return super().outputs


#internal name: elemental_to_nodal_fc
#scripting name: elemental_to_nodal_fc
class InputsElementalToNodalFc(_Inputs):
    """Intermediate class used to connect user inputs to elemental_to_nodal_fc operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.elemental_to_nodal_fc()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_force_averaging = int()
      >>> op.inputs.force_averaging.connect(my_force_averaging)
      >>> my_mesh_scoping = dpf.Scoping()
      >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    """
    def __init__(self, op: Operator):
        super().__init__(elemental_to_nodal_fc._spec().inputs, op)
        self._fields_container = Input(elemental_to_nodal_fc._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._mesh = Input(elemental_to_nodal_fc._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh)
        self._force_averaging = Input(elemental_to_nodal_fc._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._force_averaging)
        self._mesh_scoping = Input(elemental_to_nodal_fc._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._mesh_scoping)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_to_nodal_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_to_nodal_fc()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def force_averaging(self):
        """Allows to connect force_averaging input to the operator

        - pindoc: averaging on nodes is used if this pin is set to 1 (default is one for integrated results and 0 for dicrete ones)

        Parameters
        ----------
        my_force_averaging : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_to_nodal_fc()
        >>> op.inputs.force_averaging.connect(my_force_averaging)
        >>> #or
        >>> op.inputs.force_averaging(my_force_averaging)

        """
        return self._force_averaging

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator

        Parameters
        ----------
        my_mesh_scoping : Scoping, ScopingsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_to_nodal_fc()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> #or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)

        """
        return self._mesh_scoping

class OutputsElementalToNodalFc(_Outputs):
    """Intermediate class used to get outputs from elemental_to_nodal_fc operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.averaging.elemental_to_nodal_fc()
      >>> # Connect inputs : op.inputs. ...
      >>> result_fields_container = op.outputs.fields_container()
    """
    def __init__(self, op: Operator):
        super().__init__(elemental_to_nodal_fc._spec().outputs, op)
        self._fields_container = Output(elemental_to_nodal_fc._spec().output_pin(0), 0, op) 
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator


        Returns
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.averaging.elemental_to_nodal_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container() 
        """
        return self._fields_container

