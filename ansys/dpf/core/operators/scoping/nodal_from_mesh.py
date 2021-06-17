"""
nodal_from_mesh
===============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "scoping" category
"""

class nodal_from_mesh(Operator):
    """Get the nodes ids scoping of an input mesh.

      available inputs:
        - mesh (MeshedRegion)

      available outputs:
        - mesh_scoping (Scoping)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.scoping.nodal_from_mesh()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.scoping.nodal_from_mesh(mesh=my_mesh)

      >>> # Get output data
      >>> result_mesh_scoping = op.outputs.mesh_scoping()"""
    def __init__(self, mesh=None, config=None, server=None):
        super().__init__(name="GetNodeScopingFromMesh", config = config, server = server)
        self._inputs = InputsNodalFromMesh(self)
        self._outputs = OutputsNodalFromMesh(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Get the nodes ids scoping of an input mesh.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "GetNodeScopingFromMesh")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsNodalFromMesh 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsNodalFromMesh 
        """
        return super().outputs


#internal name: GetNodeScopingFromMesh
#scripting name: nodal_from_mesh
class InputsNodalFromMesh(_Inputs):
    """Intermediate class used to connect user inputs to nodal_from_mesh operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.nodal_from_mesh()
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(nodal_from_mesh._spec().inputs, op)
        self._mesh = Input(nodal_from_mesh._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._mesh)

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.nodal_from_mesh()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsNodalFromMesh(_Outputs):
    """Intermediate class used to get outputs from nodal_from_mesh operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.nodal_from_mesh()
      >>> # Connect inputs : op.inputs. ...
      >>> result_mesh_scoping = op.outputs.mesh_scoping()
    """
    def __init__(self, op: Operator):
        super().__init__(nodal_from_mesh._spec().outputs, op)
        self._mesh_scoping = Output(nodal_from_mesh._spec().output_pin(0), 0, op) 
        self._outputs.append(self._mesh_scoping)

    @property
    def mesh_scoping(self):
        """Allows to get mesh_scoping output of the operator


        Returns
        ----------
        my_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.nodal_from_mesh()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh_scoping = op.outputs.mesh_scoping() 
        """
        return self._mesh_scoping
