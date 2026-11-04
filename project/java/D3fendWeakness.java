package example;

/* metamodel_version: 1.12.0 */
/* version: 1.6.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A condition in a system component that can contribute to a vulnerability. Nearly all of these entries name a CWE entry.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class D3fendWeakness extends D3fendEntry {

  private List<D3fendArtifact> mayBeWeaknessOf;


}