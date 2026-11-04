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
  A set of D3FEND classes of which no two share an instance.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class D3fendDisjointGroup  {

  private List<D3fendEntry> members;


}